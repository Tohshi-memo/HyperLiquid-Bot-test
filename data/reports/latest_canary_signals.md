# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T03:37:27.882851+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.6043` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.507` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0094` n `12`; crypto_alt avg `-0.1991` n `233`; crypto_major avg `-0.1307` n `8`; equity avg `-0.0288` n `136`; fx avg `-0.0046` n `6`; index avg `-0.0034` n `27`; metal avg `-0.0431` n `20`; unknown avg `1.3724` n `894`
- 1h: commodity avg `0.0963` n `12`; crypto_alt avg `0.1209` n `233`; crypto_major avg `0.3772` n `8`; equity avg `-0.1037` n `136`; fx avg `-0.0127` n `6`; index avg `-0.0301` n `27`; metal avg `-0.1216` n `20`; unknown avg `0.3975` n `892`
- 4h: commodity avg `0.0744` n `12`; crypto_alt avg `1.5324` n `233`; crypto_major avg `1.583` n `8`; equity avg `0.076` n `136`; fx avg `0.0196` n `6`; index avg `-0.0364` n `27`; metal avg `-0.0213` n `20`; unknown avg `18.9115` n `768`
- 24h: commodity avg `0.7343` n `12`; crypto_alt avg `-0.5241` n `233`; crypto_major avg `-0.0195` n `8`; equity avg `-1.3827` n `136`; fx avg `0.0396` n `6`; index avg `-0.3037` n `26`; metal avg `-0.1431` n `20`; unknown avg `2.0307` n `682`

## Correlations

- market_context_score -> index_forward_1h_return_pct: corr `-0.1329`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.13`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1142`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1091`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
