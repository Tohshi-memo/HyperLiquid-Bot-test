# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T02:07:23.854824+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0189` n `12`; crypto_alt avg `-0.1303` n `230`; crypto_major avg `-0.0736` n `8`; equity avg `-0.03` n `96`; fx avg `0.0013` n `6`; index avg `0.0043` n `25`; metal avg `-0.0036` n `20`; unknown avg `0.0745` n `769`
- 1h: commodity avg `0.0507` n `12`; crypto_alt avg `-0.12` n `230`; crypto_major avg `0.0103` n `8`; equity avg `0.0304` n `96`; fx avg `-0.0221` n `6`; index avg `0.0233` n `25`; metal avg `-0.0057` n `20`; unknown avg `-0.2204` n `769`
- 4h: commodity avg `0.018` n `12`; crypto_alt avg `-0.0354` n `230`; crypto_major avg `-0.0927` n `8`; equity avg `0.1814` n `96`; fx avg `-0.0021` n `6`; index avg `0.0361` n `25`; metal avg `0.0707` n `20`; unknown avg `-0.2766` n `769`
- 24h: commodity avg `0.7068` n `12`; crypto_alt avg `-0.3145` n `230`; crypto_major avg `-0.2357` n `8`; equity avg `0.2453` n `94`; fx avg `0.0683` n `6`; index avg `-0.0281` n `25`; metal avg `0.1703` n `20`; unknown avg `0.2141` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.138`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
