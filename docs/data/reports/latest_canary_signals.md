# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T04:37:28.109289+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0055` n `12`; crypto_alt avg `-0.2447` n `228`; crypto_major avg `-0.1857` n `8`; equity avg `-0.0271` n `74`; fx avg `0.0022` n `6`; index avg `0.0167` n `23`; metal avg `0.0014` n `18`; unknown avg `-0.1344` n `645`
- 1h: commodity avg `-0.0384` n `12`; crypto_alt avg `-0.2667` n `228`; crypto_major avg `-0.1957` n `8`; equity avg `-0.0114` n `74`; fx avg `-0.0037` n `6`; index avg `0.0674` n `23`; metal avg `0.0063` n `18`; unknown avg `0.7394` n `645`
- 4h: commodity avg `-0.0171` n `12`; crypto_alt avg `-0.2532` n `228`; crypto_major avg `-0.24` n `8`; equity avg `0.0617` n `74`; fx avg `-0.0001` n `6`; index avg `0.047` n `23`; metal avg `0.1893` n `18`; unknown avg `-1.393` n `629`
- 24h: commodity avg `-0.7796` n `12`; crypto_alt avg `1.2859` n `228`; crypto_major avg `1.4757` n `8`; equity avg `0.7006` n `74`; fx avg `-0.0115` n `6`; index avg `0.3191` n `23`; metal avg `0.3358` n `18`; unknown avg `-1.5412` n `595`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0643`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0616`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0605`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0602`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0592`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0576`, n `668`, weak_sample_signal
