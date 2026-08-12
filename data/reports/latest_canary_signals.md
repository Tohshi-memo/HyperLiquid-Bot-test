# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T00:22:26.633248+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0053` n `12`; crypto_alt avg `0.0719` n `230`; crypto_major avg `0.0018` n `8`; equity avg `0.1304` n `113`; fx avg `0.0149` n `6`; index avg `0.025` n `25`; metal avg `0.0333` n `20`; unknown avg `-0.042` n `786`
- 1h: commodity avg `0.0464` n `12`; crypto_alt avg `0.0936` n `230`; crypto_major avg `0.1037` n `8`; equity avg `0.2167` n `113`; fx avg `0.0211` n `6`; index avg `0.0329` n `25`; metal avg `0.02` n `20`; unknown avg `-0.0714` n `786`
- 4h: commodity avg `0.05` n `12`; crypto_alt avg `0.0502` n `230`; crypto_major avg `0.178` n `8`; equity avg `0.3876` n `113`; fx avg `0.0217` n `6`; index avg `0.0153` n `25`; metal avg `0.0463` n `20`; unknown avg `-0.0339` n `785`
- 24h: commodity avg `0.2047` n `12`; crypto_alt avg `-1.1734` n `230`; crypto_major avg `0.7651` n `8`; equity avg `1.6106` n `113`; fx avg `-0.0483` n `6`; index avg `0.1864` n `25`; metal avg `-0.2993` n `20`; unknown avg `-0.0503` n `753`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.225`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.2184`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2144`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2031`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1974`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1574`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1429`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.125`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
