# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T23:52:29.961429+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0067` n `12`; crypto_alt avg `-0.0059` n `234`; crypto_major avg `-0.0044` n `8`; equity avg `0.0047` n `142`; fx avg `-0.0067` n `6`; index avg `0.0125` n `26`; metal avg `0.028` n `20`; unknown avg `0.4222` n `963`
- 1h: commodity avg `-0.0273` n `12`; crypto_alt avg `-0.331` n `234`; crypto_major avg `-0.1286` n `8`; equity avg `0.0454` n `142`; fx avg `-0.0167` n `6`; index avg `0.0189` n `26`; metal avg `0.0364` n `20`; unknown avg `0.4843` n `961`
- 4h: commodity avg `0.042` n `12`; crypto_alt avg `-0.2424` n `234`; crypto_major avg `0.1439` n `8`; equity avg `0.2226` n `142`; fx avg `-0.0154` n `6`; index avg `0.0647` n `26`; metal avg `0.1172` n `20`; unknown avg `2.5066` n `872`
- 24h: commodity avg `-0.8912` n `12`; crypto_alt avg `-0.2109` n `234`; crypto_major avg `-0.3308` n `8`; equity avg `0.8288` n `142`; fx avg `-0.1698` n `6`; index avg `0.1281` n `26`; metal avg `0.2872` n `20`; unknown avg `3099.2534` n `834`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1869`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1833`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1734`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1443`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1361`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1332`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1228`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1169`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1143`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1025`, n `668`, weak_sample_signal
