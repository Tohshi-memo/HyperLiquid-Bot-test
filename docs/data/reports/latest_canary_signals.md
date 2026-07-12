# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T20:52:23.172104+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0295` n `12`; crypto_alt avg `0.0044` n `230`; crypto_major avg `0.0441` n `8`; equity avg `0.0136` n `92`; fx avg `-0.004` n `6`; index avg `-0.011` n `25`; metal avg `0.0058` n `20`; unknown avg `-0.055` n `765`
- 1h: commodity avg `0.0178` n `12`; crypto_alt avg `-0.1887` n `230`; crypto_major avg `-0.1436` n `8`; equity avg `-0.0109` n `92`; fx avg `-0.0197` n `6`; index avg `-0.0166` n `25`; metal avg `-0.0017` n `20`; unknown avg `0.0291` n `765`
- 4h: commodity avg `0.073` n `12`; crypto_alt avg `-0.1207` n `230`; crypto_major avg `-0.0708` n `8`; equity avg `0.0638` n `92`; fx avg `-0.0344` n `6`; index avg `-0.0242` n `25`; metal avg `-0.0045` n `20`; unknown avg `-0.1278` n `765`
- 24h: commodity avg `0.6107` n `12`; crypto_alt avg `-1.5359` n `230`; crypto_major avg `-0.6361` n `8`; equity avg `-0.2016` n `92`; fx avg `-0.017` n `6`; index avg `-0.1003` n `25`; metal avg `-0.1094` n `20`; unknown avg `0.2087` n `741`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1775`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1625`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1298`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1287`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1214`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1059`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
