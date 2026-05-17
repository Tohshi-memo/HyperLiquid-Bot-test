# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-17T18:37:13.979551+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0228` n `12`; crypto_alt avg `0.2395` n `228`; crypto_major avg `0.2739` n `8`; equity avg `0.0135` n `65`; fx avg `0.0` n `5`; index avg `-0.0189` n `23`; metal avg `0.0004` n `18`; unknown avg `0.0988` n `384`
- 1h: commodity avg `0.0872` n `12`; crypto_alt avg `0.1703` n `228`; crypto_major avg `0.3464` n `8`; equity avg `0.0612` n `65`; fx avg `-0.0013` n `5`; index avg `0.0224` n `23`; metal avg `-0.0597` n `18`; unknown avg `0.061` n `384`
- 4h: commodity avg `0.137` n `12`; crypto_alt avg `-0.2464` n `228`; crypto_major avg `0.3428` n `8`; equity avg `0.0111` n `65`; fx avg `0.0095` n `5`; index avg `0.048` n `23`; metal avg `-0.03` n `18`; unknown avg `-0.017` n `383`
- 24h: commodity avg `1.8429` n `12`; crypto_alt avg `-9.6282` n `228`; crypto_major avg `-2.2869` n `8`; equity avg `-2.6079` n `65`; fx avg `-0.1555` n `5`; index avg `-1.5997` n `23`; metal avg `-5.8922` n `18`; unknown avg `550.0151` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1424`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0699`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0618`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0593`, n `668`, weak_sample_signal
