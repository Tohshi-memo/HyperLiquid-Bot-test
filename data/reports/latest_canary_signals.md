# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T20:52:40.301205+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.01` n `13`; crypto_alt avg `0.0961` n `238`; crypto_major avg `0.0937` n `8`; equity avg `0.0264` n `154`; fx avg `-0.0071` n `6`; index avg `0.0029` n `27`; metal avg `0.0155` n `20`; unknown avg `1.3134` n `1238`
- 1h: commodity avg `0.08` n `13`; crypto_alt avg `-0.0313` n `238`; crypto_major avg `-0.1011` n `8`; equity avg `-0.2294` n `154`; fx avg `-0.0208` n `6`; index avg `-0.009` n `27`; metal avg `0.0171` n `20`; unknown avg `0.8419` n `1158`
- 4h: commodity avg `0.1328` n `13`; crypto_alt avg `0.3215` n `238`; crypto_major avg `0.1666` n `8`; equity avg `-0.1649` n `154`; fx avg `-0.0225` n `6`; index avg `-0.0051` n `27`; metal avg `0.0601` n `20`; unknown avg `0.8715` n `1158`
- 24h: commodity avg `-0.1909` n `13`; crypto_alt avg `1.3419` n `237`; crypto_major avg `1.592` n `8`; equity avg `1.5151` n `154`; fx avg `-0.0541` n `6`; index avg `0.4152` n `27`; metal avg `0.2234` n `20`; unknown avg `23.9736` n `1042`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2334`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.2`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1989`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1635`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.108`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1036`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0994`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
