# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T09:22:23.831516+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0211` n `13`; crypto_alt avg `0.0603` n `235`; crypto_major avg `0.0537` n `8`; equity avg `-0.0061` n `143`; fx avg `-0.0102` n `6`; index avg `-0.0037` n `26`; metal avg `-0.0038` n `20`; unknown avg `1.9969` n `982`
- 1h: commodity avg `-0.023` n `13`; crypto_alt avg `0.0068` n `235`; crypto_major avg `0.047` n `8`; equity avg `-0.0026` n `143`; fx avg `-0.0109` n `6`; index avg `0.0001` n `26`; metal avg `-0.0096` n `20`; unknown avg `3.331` n `982`
- 4h: commodity avg `0.0266` n `13`; crypto_alt avg `-0.6384` n `235`; crypto_major avg `-0.1365` n `8`; equity avg `0.004` n `143`; fx avg `-0.0019` n `6`; index avg `-0.0093` n `26`; metal avg `-0.0069` n `20`; unknown avg `1.3318` n `944`
- 24h: commodity avg `0.6938` n `13`; crypto_alt avg `-2.4965` n `235`; crypto_major avg `-2.3263` n `8`; equity avg `-0.0386` n `142`; fx avg `0.0209` n `6`; index avg `0.1201` n `26`; metal avg `-0.3028` n `20`; unknown avg `0.8289` n `872`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1839`, n `669`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1731`, n `669`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1464`, n `669`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1443`, n `669`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1151`, n `669`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1151`, n `669`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1125`, n `669`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1085`, n `669`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1076`, n `669`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0868`, n `669`, weak_sample_signal
