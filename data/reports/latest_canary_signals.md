# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T11:07:22.821441+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0049` n `12`; crypto_alt avg `-0.0562` n `231`; crypto_major avg `0.0808` n `8`; equity avg `0.0138` n `128`; fx avg `-0.0019` n `6`; index avg `0.0064` n `26`; metal avg `0.0009` n `20`; unknown avg `-0.0132` n `793`
- 1h: commodity avg `0.0107` n `12`; crypto_alt avg `0.3113` n `231`; crypto_major avg `0.3115` n `8`; equity avg `0.0295` n `128`; fx avg `-0.0075` n `6`; index avg `-0.0123` n `26`; metal avg `0.0085` n `20`; unknown avg `-0.0925` n `791`
- 4h: commodity avg `-0.0147` n `12`; crypto_alt avg `0.3263` n `231`; crypto_major avg `-0.0152` n `8`; equity avg `-0.0289` n `128`; fx avg `-0.0048` n `6`; index avg `-0.0079` n `26`; metal avg `0.0` n `20`; unknown avg `-0.276` n `791`
- 24h: commodity avg `-0.0138` n `12`; crypto_alt avg `1.588` n `231`; crypto_major avg `1.0571` n `8`; equity avg `0.2858` n `128`; fx avg `0.0074` n `6`; index avg `0.0627` n `26`; metal avg `0.0986` n `20`; unknown avg `0.6006` n `718`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1284`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1245`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1241`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1171`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1141`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0703`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0654`, n `668`, weak_sample_signal
