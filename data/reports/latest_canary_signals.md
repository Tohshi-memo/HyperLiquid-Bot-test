# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T10:22:30.861323+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0176` n `13`; crypto_alt avg `-0.01` n `239`; crypto_major avg `-0.09` n `8`; equity avg `-0.1258` n `168`; fx avg `0.0119` n `6`; index avg `-0.0208` n `27`; metal avg `-0.0898` n `20`; unknown avg `0.2137` n `1265`
- 1h: commodity avg `0.0696` n `13`; crypto_alt avg `-0.0461` n `239`; crypto_major avg `0.0125` n `8`; equity avg `-0.0051` n `168`; fx avg `0.0154` n `6`; index avg `0.0095` n `27`; metal avg `-0.0773` n `20`; unknown avg `1.3434` n `1259`
- 4h: commodity avg `-0.1842` n `13`; crypto_alt avg `0.245` n `239`; crypto_major avg `0.202` n `8`; equity avg `0.0843` n `168`; fx avg `0.057` n `6`; index avg `0.0033` n `27`; metal avg `0.0174` n `20`; unknown avg `176.3258` n `1151`
- 24h: commodity avg `0.2725` n `13`; crypto_alt avg `3.6345` n `239`; crypto_major avg `3.6481` n `8`; equity avg `3.7187` n `168`; fx avg `0.1078` n `6`; index avg `0.3149` n `27`; metal avg `0.6671` n `20`; unknown avg `449.8407` n `1001`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1244`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1243`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1218`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1095`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1083`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1081`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.104`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
