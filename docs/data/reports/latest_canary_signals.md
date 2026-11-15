# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T20:37:26.133366+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0103` n `13`; crypto_alt avg `0.3698` n `239`; crypto_major avg `0.3603` n `8`; equity avg `0.0903` n `162`; fx avg `-0.0063` n `6`; index avg `0.0109` n `27`; metal avg `0.0205` n `20`; unknown avg `0.3022` n `1265`
- 1h: commodity avg `0.0047` n `13`; crypto_alt avg `0.5153` n `239`; crypto_major avg `0.2973` n `8`; equity avg `0.0928` n `162`; fx avg `0.0288` n `6`; index avg `0.0003` n `27`; metal avg `0.0441` n `20`; unknown avg `-0.1439` n `1255`
- 4h: commodity avg `0.0484` n `13`; crypto_alt avg `0.5542` n `239`; crypto_major avg `0.7421` n `8`; equity avg `0.2724` n `162`; fx avg `0.0595` n `6`; index avg `0.021` n `27`; metal avg `0.1017` n `20`; unknown avg `4.1722` n `1251`
- 24h: commodity avg `0.0851` n `13`; crypto_alt avg `1.4718` n `239`; crypto_major avg `1.2544` n `8`; equity avg `0.8631` n `162`; fx avg `0.0348` n `6`; index avg `0.0956` n `27`; metal avg `0.0888` n `20`; unknown avg `45.9172` n `1152`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1383`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1197`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1168`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1149`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
