# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T15:52:26.480213+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0035` n `12`; crypto_alt avg `-0.0293` n `230`; crypto_major avg `0.0003` n `8`; equity avg `0.2219` n `96`; fx avg `-0.0056` n `6`; index avg `0.0333` n `25`; metal avg `0.0482` n `20`; unknown avg `-0.0697` n `769`
- 1h: commodity avg `0.0195` n `12`; crypto_alt avg `0.1103` n `230`; crypto_major avg `0.1241` n `8`; equity avg `0.1913` n `96`; fx avg `0.0573` n `6`; index avg `0.1088` n `25`; metal avg `0.1769` n `20`; unknown avg `-0.1254` n `769`
- 4h: commodity avg `0.1988` n `12`; crypto_alt avg `-0.0721` n `230`; crypto_major avg `-0.2554` n `8`; equity avg `0.7963` n `96`; fx avg `0.071` n `6`; index avg `0.1674` n `25`; metal avg `0.2367` n `20`; unknown avg `-0.0766` n `769`
- 24h: commodity avg `0.4538` n `12`; crypto_alt avg `-2.0973` n `230`; crypto_major avg `-3.0109` n `8`; equity avg `-2.2927` n `94`; fx avg `0.0515` n `6`; index avg `-0.4258` n `25`; metal avg `-0.3458` n `20`; unknown avg `-0.3983` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1312`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
