# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T03:07:25.685250+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- news_risk_spike: score `70.5` - News risk is high; compare crypto drawdown vs metal/index behavior.

## Class Returns

- 15m: commodity avg `-0.029` n `12`; crypto_alt avg `-0.5759` n `230`; crypto_major avg `-0.3857` n `8`; equity avg `-0.0277` n `121`; fx avg `-0.0055` n `6`; index avg `-0.0004` n `25`; metal avg `0.002` n `20`; unknown avg `-0.0112` n `794`
- 1h: commodity avg `-0.0283` n `12`; crypto_alt avg `-0.6419` n `230`; crypto_major avg `-0.6035` n `8`; equity avg `-0.0196` n `121`; fx avg `0.0046` n `6`; index avg `0.0035` n `25`; metal avg `-0.004` n `20`; unknown avg `0.2111` n `794`
- 4h: commodity avg `-0.0523` n `12`; crypto_alt avg `-1.198` n `230`; crypto_major avg `0.0367` n `8`; equity avg `0.1875` n `121`; fx avg `0.0262` n `6`; index avg `0.0319` n `25`; metal avg `0.038` n `20`; unknown avg `2.3167` n `794`
- 24h: commodity avg `0.0541` n `12`; crypto_alt avg `-6.0468` n `230`; crypto_major avg `-2.5733` n `8`; equity avg `-0.298` n `121`; fx avg `0.1007` n `6`; index avg `-0.0403` n `25`; metal avg `-0.0221` n `20`; unknown avg `3.2566` n `777`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.139`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1192`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1164`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1142`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1132`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
