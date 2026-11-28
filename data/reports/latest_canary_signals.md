# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T18:37:30.659773+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0007` n `13`; crypto_alt avg `0.0029` n `239`; crypto_major avg `0.051` n `8`; equity avg `0.0388` n `168`; fx avg `0.0023` n `6`; index avg `0.0005` n `27`; metal avg `0.0053` n `20`; unknown avg `0.4089` n `1268`
- 1h: commodity avg `-0.0206` n `13`; crypto_alt avg `-0.0957` n `239`; crypto_major avg `-0.0888` n `8`; equity avg `0.0301` n `168`; fx avg `0.0014` n `6`; index avg `0.0027` n `27`; metal avg `-0.0015` n `20`; unknown avg `297.0595` n `1246`
- 4h: commodity avg `-0.0708` n `13`; crypto_alt avg `-0.8605` n `239`; crypto_major avg `-0.1302` n `8`; equity avg `0.0001` n `168`; fx avg `0.004` n `6`; index avg `-0.0043` n `27`; metal avg `-0.0193` n `20`; unknown avg `41.3677` n `1211`
- 24h: commodity avg `-0.1044` n `13`; crypto_alt avg `-2.9448` n `239`; crypto_major avg `-1.0107` n `8`; equity avg `-0.0253` n `168`; fx avg `-0.0067` n `6`; index avg `-0.0184` n `27`; metal avg `0.2036` n `20`; unknown avg `187.6083` n `1064`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1608`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1467`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1251`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1244`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0815`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0539`, n `668`, weak_sample_signal
