# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T00:37:25.580911+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0461` n `12`; crypto_alt avg `-0.0349` n `230`; crypto_major avg `-0.0635` n `8`; equity avg `-0.1969` n `113`; fx avg `-0.0191` n `6`; index avg `-0.0852` n `25`; metal avg `0.0459` n `20`; unknown avg `-0.086` n `786`
- 1h: commodity avg `-0.1018` n `12`; crypto_alt avg `0.4867` n `230`; crypto_major avg `0.2025` n `8`; equity avg `0.1077` n `113`; fx avg `-0.0619` n `6`; index avg `0.0098` n `25`; metal avg `0.2209` n `20`; unknown avg `0.0317` n `786`
- 4h: commodity avg `-0.1007` n `12`; crypto_alt avg `-0.2933` n `230`; crypto_major avg `-0.2844` n `8`; equity avg `0.3122` n `113`; fx avg `-0.0714` n `6`; index avg `0.0229` n `25`; metal avg `0.2041` n `20`; unknown avg `-0.1801` n `786`
- 24h: commodity avg `-0.1533` n `12`; crypto_alt avg `-1.0754` n `230`; crypto_major avg `-0.3958` n `8`; equity avg `2.814` n `113`; fx avg `-0.0544` n `6`; index avg `0.3663` n `25`; metal avg `0.295` n `20`; unknown avg `0.0668` n `770`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2383`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2028`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1895`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1878`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1851`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.171`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.158`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1423`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1393`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.137`, n `668`, weak_sample_signal
