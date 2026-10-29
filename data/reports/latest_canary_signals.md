# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T10:07:28.917483+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0893` n `13`; crypto_alt avg `0.0342` n `238`; crypto_major avg `-0.0814` n `8`; equity avg `0.1241` n `155`; fx avg `0.0108` n `6`; index avg `-0.0134` n `27`; metal avg `0.0397` n `20`; unknown avg `0.1506` n `1220`
- 1h: commodity avg `0.0498` n `13`; crypto_alt avg `0.0339` n `238`; crypto_major avg `-0.1473` n `8`; equity avg `-0.0216` n `155`; fx avg `0.0246` n `6`; index avg `0.0136` n `27`; metal avg `-0.0888` n `20`; unknown avg `-0.1513` n `1210`
- 4h: commodity avg `-0.03` n `13`; crypto_alt avg `-0.3166` n `238`; crypto_major avg `-0.3216` n `8`; equity avg `-0.1681` n `155`; fx avg `0.0297` n `6`; index avg `0.0163` n `27`; metal avg `-0.099` n `20`; unknown avg `-0.3406` n `1192`
- 24h: commodity avg `-0.1935` n `13`; crypto_alt avg `-2.63` n `238`; crypto_major avg `-2.0875` n `8`; equity avg `-1.1842` n `155`; fx avg `0.0435` n `6`; index avg `0.0532` n `27`; metal avg `-0.4097` n `20`; unknown avg `27.3888` n `998`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0837`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0651`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal
