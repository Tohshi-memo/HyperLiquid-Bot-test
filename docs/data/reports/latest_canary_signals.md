# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T04:37:24.581790+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0034` n `12`; crypto_alt avg `-0.1183` n `230`; crypto_major avg `-0.1087` n `8`; equity avg `-0.0455` n `113`; fx avg `-0.0063` n `6`; index avg `-0.0101` n `25`; metal avg `0.0082` n `20`; unknown avg `-0.2138` n `786`
- 1h: commodity avg `-0.0142` n `12`; crypto_alt avg `-0.2676` n `230`; crypto_major avg `-0.1406` n `8`; equity avg `-0.0615` n `113`; fx avg `-0.0278` n `6`; index avg `-0.0222` n `25`; metal avg `-0.0225` n `20`; unknown avg `-0.1923` n `786`
- 4h: commodity avg `0.0968` n `12`; crypto_alt avg `0.0468` n `230`; crypto_major avg `-0.0438` n `8`; equity avg `0.6319` n `113`; fx avg `0.0171` n `6`; index avg `0.1115` n `25`; metal avg `0.1062` n `20`; unknown avg `-0.3026` n `786`
- 24h: commodity avg `0.3134` n `12`; crypto_alt avg `-1.1112` n `230`; crypto_major avg `0.4768` n `8`; equity avg `1.571` n `113`; fx avg `0.0205` n `6`; index avg `0.0956` n `25`; metal avg `-0.1105` n `20`; unknown avg `-0.1272` n `753`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2222`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.2201`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2121`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2086`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1991`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1372`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1307`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1125`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1047`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
