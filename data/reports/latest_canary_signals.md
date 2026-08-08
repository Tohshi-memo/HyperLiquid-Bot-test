# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T16:37:26.267440+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0092` n `12`; crypto_alt avg `0.1289` n `230`; crypto_major avg `-0.0997` n `8`; equity avg `-0.0031` n `112`; fx avg `0.0098` n `6`; index avg `-0.005` n `25`; metal avg `0.0015` n `20`; unknown avg `5.7867` n `784`
- 1h: commodity avg `-0.0007` n `12`; crypto_alt avg `0.3406` n `230`; crypto_major avg `0.0446` n `8`; equity avg `0.0204` n `112`; fx avg `-0.0007` n `6`; index avg `-0.0258` n `25`; metal avg `0.007` n `20`; unknown avg `0.1306` n `784`
- 4h: commodity avg `-0.0393` n `12`; crypto_alt avg `0.9173` n `230`; crypto_major avg `0.5899` n `8`; equity avg `0.2086` n `112`; fx avg `-0.0056` n `6`; index avg `0.0294` n `25`; metal avg `0.0086` n `20`; unknown avg `-0.1642` n `784`
- 24h: commodity avg `-0.2941` n `12`; crypto_alt avg `1.3728` n `230`; crypto_major avg `1.0872` n `8`; equity avg `0.8331` n `112`; fx avg `0.0163` n `6`; index avg `0.0666` n `25`; metal avg `0.121` n `20`; unknown avg `-0.0597` n `750`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1171`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0711`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0686`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0637`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.059`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0561`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0559`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0548`, n `668`, weak_sample_signal
