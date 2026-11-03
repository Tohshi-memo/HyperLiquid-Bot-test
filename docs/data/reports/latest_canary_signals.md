# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T08:37:29.541962+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1272` n `13`; crypto_alt avg `-0.1071` n `239`; crypto_major avg `-0.1226` n `8`; equity avg `-0.0697` n `157`; fx avg `0.0135` n `6`; index avg `-0.0189` n `27`; metal avg `-0.0763` n `20`; unknown avg `-0.1355` n `1264`
- 1h: commodity avg `0.1157` n `13`; crypto_alt avg `-0.2544` n `239`; crypto_major avg `-0.3035` n `8`; equity avg `0.1113` n `157`; fx avg `0.0427` n `6`; index avg `0.0323` n `27`; metal avg `-0.0644` n `20`; unknown avg `0.4652` n `1242`
- 4h: commodity avg `0.4406` n `13`; crypto_alt avg `-0.7793` n `239`; crypto_major avg `-0.5414` n `8`; equity avg `-0.1982` n `157`; fx avg `0.076` n `6`; index avg `0.0026` n `27`; metal avg `-0.2742` n `20`; unknown avg `0.188` n `1208`
- 24h: commodity avg `-0.23` n `13`; crypto_alt avg `-2.7383` n `238`; crypto_major avg `-1.9762` n `8`; equity avg `-4.2438` n `157`; fx avg `0.0166` n `6`; index avg `-0.2951` n `27`; metal avg `-0.499` n `20`; unknown avg `3.9456` n `1021`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1659`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1612`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.158`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1496`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1265`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1156`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
