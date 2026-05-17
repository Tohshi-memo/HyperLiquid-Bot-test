# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-17T11:52:17.236988+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0227` n `12`; crypto_alt avg `-0.0063` n `228`; crypto_major avg `-0.0009` n `8`; equity avg `0.0078` n `65`; fx avg `-0.0006` n `5`; index avg `0.0176` n `23`; metal avg `0.013` n `18`; unknown avg `0.032` n `383`
- 1h: commodity avg `0.0014` n `12`; crypto_alt avg `-0.3424` n `228`; crypto_major avg `-0.1473` n `8`; equity avg `0.0376` n `65`; fx avg `0.0006` n `5`; index avg `0.0176` n `23`; metal avg `-0.0231` n `18`; unknown avg `-0.0916` n `383`
- 4h: commodity avg `0.0231` n `12`; crypto_alt avg `-0.2045` n `228`; crypto_major avg `0.3062` n `8`; equity avg `0.3021` n `65`; fx avg `0.0053` n `5`; index avg `0.1594` n `23`; metal avg `-0.0567` n `18`; unknown avg `0.0126` n `383`
- 24h: commodity avg `1.7553` n `12`; crypto_alt avg `-8.9971` n `228`; crypto_major avg `-2.271` n `8`; equity avg `-2.6019` n `65`; fx avg `-0.1676` n `5`; index avg `-1.6488` n `23`; metal avg `-5.8501` n `18`; unknown avg `550.1117` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.14`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1182`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0727`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0706`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0659`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0639`, n `668`, weak_sample_signal
