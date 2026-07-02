# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-02T21:37:36.311451+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0003` n `12`; crypto_alt avg `0.0153` n `229`; crypto_major avg `-0.0948` n `8`; equity avg `0.0488` n `88`; fx avg `-0.0107` n `6`; index avg `0.0028` n `25`; metal avg `-0.0082` n `20`; unknown avg `-0.1749` n `765`
- 1h: commodity avg `0.0185` n `12`; crypto_alt avg `0.2046` n `229`; crypto_major avg `0.0445` n `8`; equity avg `-0.0253` n `88`; fx avg `-0.0098` n `6`; index avg `0.0104` n `25`; metal avg `0.014` n `20`; unknown avg `-0.578` n `765`
- 4h: commodity avg `0.0624` n `12`; crypto_alt avg `0.1779` n `229`; crypto_major avg `-0.1084` n `8`; equity avg `0.6776` n `88`; fx avg `0.0483` n `6`; index avg `0.1854` n `25`; metal avg `0.1672` n `20`; unknown avg `-0.1574` n `765`
- 24h: commodity avg `0.0957` n `12`; crypto_alt avg `1.3254` n `228`; crypto_major avg `2.0738` n `8`; equity avg `-2.3972` n `88`; fx avg `-0.1236` n `6`; index avg `-0.469` n `25`; metal avg `1.0051` n `20`; unknown avg `1.5358` n `739`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.065`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0622`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0617`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0598`, n `668`, weak_sample_signal
