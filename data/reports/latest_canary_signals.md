# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T10:22:19.071360+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0622` n `12`; crypto_alt avg `0.2042` n `228`; crypto_major avg `-0.0146` n `8`; equity avg `0.0073` n `67`; fx avg `-0.0012` n `6`; index avg `0.0235` n `23`; metal avg `0.0669` n `18`; unknown avg `-0.0785` n `397`
- 1h: commodity avg `-0.1345` n `12`; crypto_alt avg `0.3552` n `228`; crypto_major avg `0.0532` n `8`; equity avg `0.1155` n `67`; fx avg `-0.0114` n `6`; index avg `0.0265` n `23`; metal avg `0.3385` n `18`; unknown avg `-0.0757` n `397`
- 4h: commodity avg `-0.0511` n `12`; crypto_alt avg `0.7973` n `228`; crypto_major avg `0.4971` n `8`; equity avg `0.2885` n `67`; fx avg `0.0383` n `6`; index avg `0.112` n `23`; metal avg `0.572` n `18`; unknown avg `-0.0634` n `397`
- 24h: commodity avg `-0.174` n `12`; crypto_alt avg `0.7373` n `228`; crypto_major avg `0.0575` n `8`; equity avg `0.5559` n `67`; fx avg `0.0007` n `6`; index avg `-0.0113` n `23`; metal avg `0.7245` n `18`; unknown avg `1.0127` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1352`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1336`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1311`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1181`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.117`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1152`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1125`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
