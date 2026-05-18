# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T11:52:17.049137+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2754` n `12`; crypto_alt avg `0.5105` n `228`; crypto_major avg `0.5425` n `8`; equity avg `0.2898` n `66`; fx avg `-0.0361` n `5`; index avg `0.1843` n `23`; metal avg `0.252` n `18`; unknown avg `0.2757` n `383`
- 1h: commodity avg `-0.5388` n `12`; crypto_alt avg `0.5741` n `228`; crypto_major avg `0.4986` n `8`; equity avg `0.1608` n `66`; fx avg `-0.0179` n `5`; index avg `0.0041` n `23`; metal avg `0.4404` n `18`; unknown avg `0.0301` n `383`
- 4h: commodity avg `-0.3784` n `12`; crypto_alt avg `0.4935` n `228`; crypto_major avg `0.3715` n `8`; equity avg `0.3767` n `66`; fx avg `0.0268` n `5`; index avg `0.1378` n `23`; metal avg `0.4832` n `18`; unknown avg `-0.1633` n `383`
- 24h: commodity avg `0.2898` n `12`; crypto_alt avg `-2.5135` n `228`; crypto_major avg `-1.3352` n `8`; equity avg `0.1257` n `65`; fx avg `0.0652` n `5`; index avg `0.0741` n `23`; metal avg `0.4468` n `18`; unknown avg `-0.5321` n `363`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1455`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.131`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.127`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
