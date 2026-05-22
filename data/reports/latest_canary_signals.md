# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-22T12:52:15.795868+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0695` n `12`; crypto_alt avg `0.399` n `228`; crypto_major avg `0.1317` n `8`; equity avg `0.0878` n `67`; fx avg `0.0025` n `6`; index avg `0.0375` n `23`; metal avg `0.1843` n `18`; unknown avg `0.0729` n `386`
- 1h: commodity avg `-0.4859` n `12`; crypto_alt avg `0.5159` n `228`; crypto_major avg `0.5068` n `8`; equity avg `0.2251` n `67`; fx avg `-0.0042` n `6`; index avg `0.1336` n `23`; metal avg `-0.4193` n `18`; unknown avg `0.5976` n `386`
- 4h: commodity avg `-0.8415` n `12`; crypto_alt avg `0.857` n `228`; crypto_major avg `0.7993` n `8`; equity avg `-0.0603` n `67`; fx avg `-0.0369` n `6`; index avg `-0.0923` n `23`; metal avg `-0.1509` n `18`; unknown avg `0.4609` n `386`
- 24h: commodity avg `-1.7723` n `12`; crypto_alt avg `3.1591` n `228`; crypto_major avg `1.623` n `8`; equity avg `1.6146` n `67`; fx avg `0.087` n `6`; index avg `1.048` n `23`; metal avg `0.6043` n `18`; unknown avg `1.5082` n `375`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0585`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0463`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0421`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0404`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.04`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.04`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0372`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0357`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0353`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0336`, n `668`, weak_sample_signal
