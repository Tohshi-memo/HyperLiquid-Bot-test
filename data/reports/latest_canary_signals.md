# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-17T13:37:16.748472+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0025` n `12`; crypto_alt avg `0.2023` n `228`; crypto_major avg `0.1453` n `8`; equity avg `0.0037` n `65`; fx avg `0.0` n `5`; index avg `-0.0401` n `23`; metal avg `-0.0345` n `18`; unknown avg `-0.0318` n `383`
- 1h: commodity avg `0.0361` n `12`; crypto_alt avg `-0.2862` n `228`; crypto_major avg `-0.3849` n `8`; equity avg `-0.0421` n `65`; fx avg `-0.0024` n `5`; index avg `0.0481` n `23`; metal avg `-0.0107` n `18`; unknown avg `-0.0985` n `383`
- 4h: commodity avg `0.0233` n `12`; crypto_alt avg `-0.2284` n `228`; crypto_major avg `0.2193` n `8`; equity avg `0.2348` n `65`; fx avg `-0.0179` n `5`; index avg `0.0872` n `23`; metal avg `-0.0086` n `18`; unknown avg `-0.2417` n `383`
- 24h: commodity avg `1.8126` n `12`; crypto_alt avg `-9.1619` n `228`; crypto_major avg `-2.3972` n `8`; equity avg `-2.5683` n `65`; fx avg `-0.1861` n `5`; index avg `-1.6727` n `23`; metal avg `-5.8636` n `18`; unknown avg `550.053` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1366`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0704`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0651`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0636`, n `668`, weak_sample_signal
