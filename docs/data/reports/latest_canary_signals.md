# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T07:37:29.800135+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0034` n `12`; crypto_alt avg `-0.1852` n `233`; crypto_major avg `-0.218` n `8`; equity avg `-0.0377` n `136`; fx avg `0.0` n `6`; index avg `-0.0024` n `27`; metal avg `0.0001` n `20`; unknown avg `0.2554` n `838`
- 1h: commodity avg `0.0105` n `12`; crypto_alt avg `-0.2582` n `233`; crypto_major avg `-0.3211` n `8`; equity avg `-0.1375` n `136`; fx avg `0.0008` n `6`; index avg `-0.0139` n `26`; metal avg `-0.01` n `20`; unknown avg `0.1515` n `836`
- 4h: commodity avg `0.0852` n `12`; crypto_alt avg `-0.2514` n `233`; crypto_major avg `-0.4832` n `8`; equity avg `-0.4636` n `136`; fx avg `-0.0223` n `6`; index avg `-0.0689` n `26`; metal avg `-0.0021` n `20`; unknown avg `51.414` n `804`
- 24h: commodity avg `0.1864` n `12`; crypto_alt avg `0.2477` n `233`; crypto_major avg `-0.57` n `8`; equity avg `-0.8775` n `136`; fx avg `-0.0115` n `6`; index avg `-0.1406` n `26`; metal avg `0.0241` n `20`; unknown avg `0.6159` n `708`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0669`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0617`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0581`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0566`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0518`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0513`, n `668`, weak_sample_signal
