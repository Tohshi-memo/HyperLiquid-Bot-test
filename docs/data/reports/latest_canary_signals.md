# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T11:07:25.454771+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.051` n `12`; crypto_alt avg `-0.0362` n `230`; crypto_major avg `-0.1007` n `8`; equity avg `-0.1545` n `94`; fx avg `-0.0172` n `6`; index avg `-0.0199` n `25`; metal avg `-0.0578` n `20`; unknown avg `-0.0309` n `768`
- 1h: commodity avg `-0.0246` n `12`; crypto_alt avg `0.0331` n `230`; crypto_major avg `-0.1499` n `8`; equity avg `-0.2771` n `94`; fx avg `-0.0224` n `6`; index avg `-0.0405` n `25`; metal avg `-0.0797` n `20`; unknown avg `-0.0829` n `768`
- 4h: commodity avg `0.0591` n `12`; crypto_alt avg `-0.7965` n `230`; crypto_major avg `-1.107` n `8`; equity avg `-0.9108` n `94`; fx avg `-0.0508` n `6`; index avg `-0.1253` n `25`; metal avg `-0.0909` n `20`; unknown avg `-0.2502` n `762`
- 24h: commodity avg `-0.0852` n `12`; crypto_alt avg `-0.6594` n `230`; crypto_major avg `-0.9112` n `8`; equity avg `-3.0483` n `93`; fx avg `0.0173` n `6`; index avg `-0.5121` n `25`; metal avg `0.0059` n `20`; unknown avg `-0.0598` n `745`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1541`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1181`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1087`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1046`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0995`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
