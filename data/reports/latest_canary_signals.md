# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T23:37:25.794192+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.026` n `12`; crypto_alt avg `0.0086` n `228`; crypto_major avg `0.0443` n `8`; equity avg `-0.1192` n `86`; fx avg `0.0084` n `6`; index avg `-0.0172` n `23`; metal avg `-0.0852` n `20`; unknown avg `0.1804` n `764`
- 1h: commodity avg `-0.073` n `12`; crypto_alt avg `-0.1404` n `228`; crypto_major avg `0.0785` n `8`; equity avg `-0.2079` n `86`; fx avg `0.0103` n `6`; index avg `-0.0093` n `23`; metal avg `-0.1236` n `20`; unknown avg `0.4787` n `756`
- 4h: commodity avg `-0.1306` n `12`; crypto_alt avg `0.3092` n `228`; crypto_major avg `0.454` n `8`; equity avg `-0.2173` n `86`; fx avg `-0.0059` n `6`; index avg `0.0469` n `23`; metal avg `-0.2642` n `20`; unknown avg `0.2627` n `756`
- 24h: commodity avg `-0.4919` n `12`; crypto_alt avg `-2.0146` n `228`; crypto_major avg `-3.0024` n `8`; equity avg `-3.3471` n `86`; fx avg `-0.2144` n `6`; index avg `-0.8833` n `23`; metal avg `-1.408` n `20`; unknown avg `0.712` n `588`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1391`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1296`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1276`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0678`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0653`, n `668`, weak_sample_signal
