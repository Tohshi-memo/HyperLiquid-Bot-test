# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-26T13:52:36.988093+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0739` n `13`; crypto_alt avg `-0.3905` n `237`; crypto_major avg `-0.3085` n `8`; equity avg `-0.0166` n `152`; fx avg `-0.0061` n `6`; index avg `-0.0158` n `26`; metal avg `-0.097` n `20`; unknown avg `-0.1826` n `1242`
- 1h: commodity avg `0.0939` n `13`; crypto_alt avg `-0.4802` n `237`; crypto_major avg `-0.6137` n `8`; equity avg `-0.4612` n `152`; fx avg `-0.0137` n `6`; index avg `0.001` n `26`; metal avg `-0.1876` n `20`; unknown avg `3.4752` n `1222`
- 4h: commodity avg `0.1263` n `13`; crypto_alt avg `-0.2578` n `237`; crypto_major avg `-0.5217` n `8`; equity avg `-0.2199` n `152`; fx avg `-0.013` n `6`; index avg `0.0133` n `26`; metal avg `-0.2556` n `20`; unknown avg `4.4362` n `1216`
- 24h: commodity avg `-0.2444` n `13`; crypto_alt avg `-0.049` n `237`; crypto_major avg `-0.2813` n `8`; equity avg `-0.4054` n `152`; fx avg `0.013` n `6`; index avg `0.0548` n `26`; metal avg `-0.0538` n `20`; unknown avg `0.407` n `959`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2395`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2019`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1964`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1835`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1403`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1327`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1271`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0976`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
