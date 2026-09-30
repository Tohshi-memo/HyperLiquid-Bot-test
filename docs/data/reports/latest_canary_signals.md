# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-30T09:37:33.367936+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0867` n `12`; crypto_alt avg `0.3533` n `234`; crypto_major avg `0.3848` n `8`; equity avg `0.0416` n `142`; fx avg `0.0089` n `6`; index avg `0.0024` n `26`; metal avg `0.0183` n `20`; unknown avg `0.151` n `963`
- 1h: commodity avg `0.0875` n `12`; crypto_alt avg `1.0092` n `234`; crypto_major avg `0.8533` n `8`; equity avg `-0.0642` n `142`; fx avg `0.0359` n `6`; index avg `-0.0337` n `26`; metal avg `-0.1291` n `20`; unknown avg `2.5825` n `961`
- 4h: commodity avg `0.1178` n `12`; crypto_alt avg `0.6718` n `234`; crypto_major avg `0.3776` n `8`; equity avg `0.0152` n `142`; fx avg `0.0436` n `6`; index avg `-0.0107` n `26`; metal avg `0.0553` n `20`; unknown avg `1.5278` n `915`
- 24h: commodity avg `-0.4351` n `12`; crypto_alt avg `0.4318` n `234`; crypto_major avg `-0.4561` n `8`; equity avg `0.3743` n `142`; fx avg `-0.0124` n `6`; index avg `0.1066` n `26`; metal avg `0.2199` n `20`; unknown avg `2917.5247` n `826`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1595`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1459`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1349`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1324`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1281`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1146`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1107`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1083`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1025`, n `668`, weak_sample_signal
