# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-26T17:52:36.989123+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0085` n `13`; crypto_alt avg `-0.2874` n `237`; crypto_major avg `-0.1651` n `8`; equity avg `0.0274` n `154`; fx avg `-0.0006` n `6`; index avg `-0.0116` n `27`; metal avg `-0.036` n `20`; unknown avg `0.0382` n `1238`
- 1h: commodity avg `-0.2172` n `13`; crypto_alt avg `0.353` n `237`; crypto_major avg `0.4782` n `8`; equity avg `0.3539` n `154`; fx avg `-0.0051` n `6`; index avg `0.0368` n `27`; metal avg `0.0006` n `20`; unknown avg `-0.1043` n `1238`
- 4h: commodity avg `0.0758` n `13`; crypto_alt avg `0.5868` n `237`; crypto_major avg `0.8933` n `8`; equity avg `1.4977` n `154`; fx avg `0.0297` n `6`; index avg `0.1475` n `27`; metal avg `0.187` n `20`; unknown avg `621.5956` n `1166`
- 24h: commodity avg `-0.1856` n `13`; crypto_alt avg `-0.5068` n `237`; crypto_major avg `-0.0399` n `8`; equity avg `0.8043` n `153`; fx avg `0.0571` n `6`; index avg `-0.073` n `27`; metal avg `0.059` n `20`; unknown avg `780.4125` n `924`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2215`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.191`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1869`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.134`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1207`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1145`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1138`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
