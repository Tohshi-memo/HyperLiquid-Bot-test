# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T22:22:23.754407+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0107` n `12`; crypto_alt avg `0.0162` n `231`; crypto_major avg `-0.0373` n `8`; equity avg `0.0675` n `127`; fx avg `0.0081` n `6`; index avg `0.0001` n `26`; metal avg `0.0451` n `20`; unknown avg `-0.0134` n `792`
- 1h: commodity avg `0.0037` n `12`; crypto_alt avg `0.1865` n `231`; crypto_major avg `0.2697` n `8`; equity avg `-0.0654` n `127`; fx avg `0.0126` n `6`; index avg `-0.0116` n `26`; metal avg `0.0457` n `20`; unknown avg `-0.1813` n `792`
- 4h: commodity avg `-0.068` n `12`; crypto_alt avg `0.6332` n `231`; crypto_major avg `0.7728` n `8`; equity avg `0.0826` n `127`; fx avg `0.008` n `6`; index avg `0.0552` n `26`; metal avg `0.0756` n `20`; unknown avg `-0.0476` n `792`
- 24h: commodity avg `0.3563` n `12`; crypto_alt avg `1.5564` n `231`; crypto_major avg `2.3161` n `8`; equity avg `-0.2207` n `127`; fx avg `-0.024` n `6`; index avg `-0.1151` n `26`; metal avg `0.1234` n `20`; unknown avg `0.9064` n `775`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1308`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1251`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0815`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.064`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0628`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0536`, n `668`, weak_sample_signal
