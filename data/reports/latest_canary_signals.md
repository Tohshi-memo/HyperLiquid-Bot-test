# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T09:15:21.633596+00:00`
- Correlation status: `ready`
- Asset price records: `252`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1515` n `7`; crypto_alt avg `0.1431` n `223`; crypto_major avg `0.1369` n `7`; equity avg `0.1287` n `42`; fx avg `-0.0035` n `4`; index avg `-0.0551` n `9`; metal avg `0.1291` n `7`; unknown avg `0.1763` n `314`
- 1h: commodity avg `-0.3945` n `7`; crypto_alt avg `-0.008` n `223`; crypto_major avg `-0.0479` n `7`; equity avg `0.0604` n `42`; fx avg `0.0117` n `4`; index avg `-0.0931` n `9`; metal avg `0.0749` n `7`; unknown avg `-0.0349` n `314`
- 4h: commodity avg `0.3714` n `7`; crypto_alt avg `-0.0598` n `223`; crypto_major avg `-0.7097` n `7`; equity avg `-0.2386` n `42`; fx avg `0.0183` n `4`; index avg `-0.1525` n `9`; metal avg `-0.9415` n `7`; unknown avg `-0.1333` n `312`
- 24h: commodity avg `0.4246` n `7`; crypto_alt avg `2.1303` n `223`; crypto_major avg `1.9281` n `7`; equity avg `1.1227` n `42`; fx avg `-0.0491` n `4`; index avg `0.6913` n `9`; metal avg `-0.9006` n `7`; unknown avg `0.2012` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.3355`, n `248`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3247`, n `248`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.287`, n `244`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.2828`, n `244`, moderate_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.2205`, n `244`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.2075`, n `244`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1952`, n `248`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1839`, n `244`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1784`, n `248`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1722`, n `248`, weak_sample_signal
