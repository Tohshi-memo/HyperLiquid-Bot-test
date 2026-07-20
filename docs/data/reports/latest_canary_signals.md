# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T06:22:31.064259+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0226` n `12`; crypto_alt avg `0.114` n `230`; crypto_major avg `0.0288` n `8`; equity avg `-0.079` n `98`; fx avg `-0.0055` n `6`; index avg `0.0156` n `25`; metal avg `0.0132` n `20`; unknown avg `0.0245` n `769`
- 1h: commodity avg `0.1173` n `12`; crypto_alt avg `0.1107` n `230`; crypto_major avg `-0.0315` n `8`; equity avg `-0.1855` n `98`; fx avg `-0.0278` n `6`; index avg `0.0007` n `25`; metal avg `-0.0316` n `20`; unknown avg `-0.0026` n `753`
- 4h: commodity avg `0.0827` n `12`; crypto_alt avg `-0.6758` n `230`; crypto_major avg `-0.5919` n `8`; equity avg `0.0129` n `98`; fx avg `-0.0395` n `6`; index avg `0.0318` n `25`; metal avg `-0.0102` n `20`; unknown avg `-0.3061` n `753`
- 24h: commodity avg `0.0715` n `12`; crypto_alt avg `-0.6469` n `230`; crypto_major avg `-0.5842` n `8`; equity avg `-0.1354` n `97`; fx avg `-0.0655` n `6`; index avg `0.0085` n `25`; metal avg `-0.0195` n `20`; unknown avg `-0.1381` n `751`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1497`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.123`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1078`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.102`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0974`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0932`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0906`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0888`, n `666`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0846`, n `666`, weak_sample_signal
