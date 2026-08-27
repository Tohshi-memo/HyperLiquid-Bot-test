# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T11:07:24.517050+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0385` n `12`; crypto_alt avg `0.3786` n `231`; crypto_major avg `0.3393` n `8`; equity avg `0.1115` n `127`; fx avg `-0.0046` n `6`; index avg `0.0342` n `26`; metal avg `0.005` n `20`; unknown avg `-0.0175` n `792`
- 1h: commodity avg `-0.0167` n `12`; crypto_alt avg `-0.4825` n `231`; crypto_major avg `-0.5917` n `8`; equity avg `-0.0354` n `127`; fx avg `-0.0082` n `6`; index avg `0.0176` n `26`; metal avg `0.0823` n `20`; unknown avg `0.0743` n `792`
- 4h: commodity avg `0.3132` n `12`; crypto_alt avg `0.8515` n `231`; crypto_major avg `1.3774` n `8`; equity avg `0.5209` n `127`; fx avg `-0.0145` n `6`; index avg `0.0471` n `26`; metal avg `-0.1106` n `20`; unknown avg `0.1727` n `791`
- 24h: commodity avg `0.4693` n `12`; crypto_alt avg `1.0453` n `231`; crypto_major avg `1.4648` n `8`; equity avg `1.8795` n `127`; fx avg `-0.0828` n `6`; index avg `0.2838` n `26`; metal avg `-0.3812` n `20`; unknown avg `0.4599` n `775`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1191`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1049`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0668`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0654`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
