# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T04:22:26.238378+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0533` n `12`; crypto_alt avg `0.0648` n `230`; crypto_major avg `0.0135` n `8`; equity avg `-0.0168` n `92`; fx avg `-0.0091` n `6`; index avg `-0.0245` n `25`; metal avg `-0.0046` n `20`; unknown avg `-0.1533` n `766`
- 1h: commodity avg `-0.081` n `12`; crypto_alt avg `0.5837` n `230`; crypto_major avg `0.5894` n `8`; equity avg `0.6606` n `92`; fx avg `-0.023` n `6`; index avg `0.1935` n `25`; metal avg `0.1125` n `20`; unknown avg `0.102` n `766`
- 4h: commodity avg `-0.2226` n `12`; crypto_alt avg `0.0888` n `230`; crypto_major avg `0.0906` n `8`; equity avg `-0.2955` n `92`; fx avg `-0.0769` n `6`; index avg `-0.0456` n `25`; metal avg `0.2455` n `20`; unknown avg `-0.4733` n `766`
- 24h: commodity avg `0.9855` n `12`; crypto_alt avg `-0.4647` n `230`; crypto_major avg `-0.9491` n `8`; equity avg `-1.3736` n `92`; fx avg `-0.2227` n `6`; index avg `-0.2697` n `25`; metal avg `0.023` n `20`; unknown avg `-0.3367` n `750`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1944`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1857`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1199`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1178`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1174`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0781`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.074`, n `668`, weak_sample_signal
