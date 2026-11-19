# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-19T19:07:28.174612+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `2.6514` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.1497` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.055` n `13`; crypto_alt avg `-0.2927` n `239`; crypto_major avg `-0.5334` n `8`; equity avg `-0.4584` n `165`; fx avg `-0.0176` n `6`; index avg `-0.0436` n `27`; metal avg `-0.0523` n `20`; unknown avg `0.4799` n `1254`
- 1h: commodity avg `-0.0978` n `13`; crypto_alt avg `0.2093` n `239`; crypto_major avg `-0.0742` n `8`; equity avg `-0.3191` n `165`; fx avg `0.0064` n `6`; index avg `-0.0282` n `27`; metal avg `-0.0267` n `20`; unknown avg `0.7222` n `1256`
- 4h: commodity avg `-0.146` n `13`; crypto_alt avg `-1.7159` n `239`; crypto_major avg `-1.6225` n `8`; equity avg `-4.2739` n `165`; fx avg `-0.0236` n `6`; index avg `-0.4728` n `27`; metal avg `-0.4597` n `20`; unknown avg `19.4307` n `1251`
- 24h: commodity avg `0.1106` n `13`; crypto_alt avg `-0.3347` n `239`; crypto_major avg `0.3483` n `8`; equity avg `-1.3201` n `165`; fx avg `-0.0043` n `6`; index avg `-0.0587` n `27`; metal avg `-0.4822` n `20`; unknown avg `4.8107` n `1156`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1614`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1589`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1278`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0714`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0602`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0586`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0556`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0489`, n `668`, weak_sample_signal
