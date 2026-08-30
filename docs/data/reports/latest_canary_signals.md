# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T16:52:27.102290+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.001` n `12`; crypto_alt avg `0.0569` n `231`; crypto_major avg `0.0347` n `8`; equity avg `0.0179` n `128`; fx avg `0.0007` n `6`; index avg `0.0045` n `26`; metal avg `0.013` n `20`; unknown avg `-0.027` n `793`
- 1h: commodity avg `0.022` n `12`; crypto_alt avg `0.7796` n `231`; crypto_major avg `0.7803` n `8`; equity avg `0.1354` n `128`; fx avg `0.0009` n `6`; index avg `0.0183` n `26`; metal avg `0.051` n `20`; unknown avg `0.6864` n `793`
- 4h: commodity avg `0.0238` n `12`; crypto_alt avg `0.5749` n `231`; crypto_major avg `0.9693` n `8`; equity avg `0.1408` n `128`; fx avg `0.0032` n `6`; index avg `0.0184` n `26`; metal avg `0.1257` n `20`; unknown avg `0.2409` n `793`
- 24h: commodity avg `0.0166` n `12`; crypto_alt avg `1.4699` n `231`; crypto_major avg `1.2553` n `8`; equity avg `0.4031` n `128`; fx avg `0.0238` n `6`; index avg `0.0972` n `26`; metal avg `0.1503` n `20`; unknown avg `0.1121` n `740`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1282`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1231`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1158`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0605`, n `668`, weak_sample_signal
