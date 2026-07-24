# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T14:07:15.639038+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_crypto_equity_divergence: score `1.6522` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.1064` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0316` n `12`; crypto_alt avg `0.0244` n `230`; crypto_major avg `0.0564` n `8`; equity avg `0.0509` n `100`; fx avg `-0.0016` n `6`; index avg `0.0082` n `25`; metal avg `-0.0358` n `20`; unknown avg `0.0619` n `773`
- 1h: commodity avg `-0.107` n `12`; crypto_alt avg `0.0855` n `230`; crypto_major avg `-0.1024` n `8`; equity avg `-1.7546` n `100`; fx avg `0.0061` n `6`; index avg `-0.1622` n `25`; metal avg `0.0029` n `20`; unknown avg `-0.0797` n `773`
- 4h: commodity avg `0.1427` n `12`; crypto_alt avg `-1.347` n `230`; crypto_major avg `-1.344` n `8`; equity avg `-2.1972` n `100`; fx avg `-0.0096` n `6`; index avg `-0.2376` n `25`; metal avg `-0.1631` n `20`; unknown avg `-0.249` n `773`
- 24h: commodity avg `-0.3083` n `12`; crypto_alt avg `-1.8824` n `230`; crypto_major avg `-1.8511` n `8`; equity avg `-3.2489` n `100`; fx avg `-0.1524` n `6`; index avg `-0.4416` n `25`; metal avg `-0.0885` n `20`; unknown avg `0.1398` n `756`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1631`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1547`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1175`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1111`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1057`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1019`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0992`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
