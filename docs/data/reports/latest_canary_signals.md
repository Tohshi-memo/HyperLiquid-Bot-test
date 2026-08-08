# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T14:37:25.542190+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0231` n `12`; crypto_alt avg `0.1972` n `230`; crypto_major avg `0.3668` n `8`; equity avg `0.0202` n `112`; fx avg `-0.0032` n `6`; index avg `0.0038` n `25`; metal avg `0.0012` n `20`; unknown avg `0.0058` n `784`
- 1h: commodity avg `-0.0355` n `12`; crypto_alt avg `0.377` n `230`; crypto_major avg `0.6265` n `8`; equity avg `0.0453` n `112`; fx avg `-0.0033` n `6`; index avg `0.0007` n `25`; metal avg `-0.0014` n `20`; unknown avg `-0.0184` n `784`
- 4h: commodity avg `0.009` n `12`; crypto_alt avg `0.6011` n `230`; crypto_major avg `0.7412` n `8`; equity avg `0.2011` n `112`; fx avg `-0.0078` n `6`; index avg `0.0526` n `25`; metal avg `-0.0328` n `20`; unknown avg `-0.2742` n `784`
- 24h: commodity avg `-0.0776` n `12`; crypto_alt avg `0.8101` n `230`; crypto_major avg `0.668` n `8`; equity avg `1.1499` n `112`; fx avg `-0.0108` n `6`; index avg `0.1098` n `25`; metal avg `0.044` n `20`; unknown avg `-0.0919` n `750`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1194`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0617`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0586`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0535`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0525`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0498`, n `668`, weak_sample_signal
