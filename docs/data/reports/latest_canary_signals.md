# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T10:07:23.442065+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.046` n `12`; crypto_alt avg `-0.1316` n `228`; crypto_major avg `-0.2398` n `8`; equity avg `-0.065` n `74`; fx avg `0.0076` n `6`; index avg `-0.061` n `23`; metal avg `-0.0142` n `18`; unknown avg `0.9266` n `424`
- 1h: commodity avg `-0.0068` n `12`; crypto_alt avg `1.0256` n `228`; crypto_major avg `0.4233` n `8`; equity avg `0.2172` n `74`; fx avg `0.0083` n `6`; index avg `0.0384` n `23`; metal avg `0.1595` n `18`; unknown avg `1.5848` n `424`
- 4h: commodity avg `-0.1893` n `12`; crypto_alt avg `-0.4835` n `228`; crypto_major avg `0.1728` n `8`; equity avg `0.2549` n `74`; fx avg `0.0647` n `6`; index avg `0.0002` n `23`; metal avg `0.4877` n `18`; unknown avg `0.7962` n `424`
- 24h: commodity avg `-0.2972` n `12`; crypto_alt avg `-3.3914` n `228`; crypto_major avg `-2.4274` n `8`; equity avg `-0.3696` n `73`; fx avg `0.0952` n `6`; index avg `-0.0755` n `23`; metal avg `-0.4972` n `18`; unknown avg `1.4798` n `402`

## Correlations

- market_context_score -> index_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.094`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
