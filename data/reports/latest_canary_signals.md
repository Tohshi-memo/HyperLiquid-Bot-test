# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T01:07:33.304956+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.076` n `13`; crypto_alt avg `-0.2302` n `234`; crypto_major avg `-0.158` n `8`; equity avg `-0.1067` n `142`; fx avg `-0.0092` n `6`; index avg `-0.0241` n `26`; metal avg `-0.0873` n `20`; unknown avg `0.1049` n `983`
- 1h: commodity avg `-0.1279` n `13`; crypto_alt avg `-0.0803` n `234`; crypto_major avg `-0.0257` n `8`; equity avg `0.0241` n `142`; fx avg `0.0106` n `6`; index avg `0.0146` n `26`; metal avg `-0.1991` n `20`; unknown avg `0.0845` n `983`
- 4h: commodity avg `-0.154` n `13`; crypto_alt avg `-0.0832` n `234`; crypto_major avg `0.034` n `8`; equity avg `0.0665` n `142`; fx avg `0.041` n `6`; index avg `0.0145` n `26`; metal avg `-0.1928` n `20`; unknown avg `-0.2014` n `937`
- 24h: commodity avg `-0.0157` n `13`; crypto_alt avg `-0.6831` n `234`; crypto_major avg `-0.0526` n `8`; equity avg `0.8865` n `142`; fx avg `-0.1827` n `6`; index avg `0.1194` n `26`; metal avg `-0.1758` n `20`; unknown avg `0.1504` n `840`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1384`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1185`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.117`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1169`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
