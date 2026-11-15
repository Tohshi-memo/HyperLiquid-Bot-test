# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T05:52:23.199272+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `4.2794` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `4.2126` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `3.5444` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0076` n `13`; crypto_alt avg `0.1364` n `239`; crypto_major avg `0.0567` n `8`; equity avg `-0.0253` n `162`; fx avg `-0.0006` n `6`; index avg `-0.006` n `27`; metal avg `0.0088` n `20`; unknown avg `0.0358` n `1263`
- 1h: commodity avg `0.0147` n `13`; crypto_alt avg `-0.2434` n `239`; crypto_major avg `-0.5661` n `8`; equity avg `-0.1043` n `162`; fx avg `0.0085` n `6`; index avg `-0.0084` n `27`; metal avg `-0.0097` n `20`; unknown avg `111.5696` n `1261`
- 4h: commodity avg `0.0554` n `13`; crypto_alt avg `3.347` n `239`; crypto_major avg `4.3348` n `8`; equity avg `0.7904` n `162`; fx avg `0.0087` n `6`; index avg `0.0277` n `27`; metal avg `0.1222` n `20`; unknown avg `106.8009` n `1241`
- 24h: commodity avg `0.0837` n `13`; crypto_alt avg `-5.5137` n `239`; crypto_major avg `-4.1566` n `8`; equity avg `-0.871` n `162`; fx avg `0.045` n `6`; index avg `-0.0872` n `27`; metal avg `-0.4408` n `20`; unknown avg `46.9794` n `1060`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.156`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.117`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1158`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1139`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal
