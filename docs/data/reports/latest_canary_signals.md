# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-02T09:07:36.078642+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0516` n `13`; crypto_alt avg `0.1227` n `238`; crypto_major avg `0.0521` n `8`; equity avg `0.0434` n `156`; fx avg `0.008` n `6`; index avg `0.0131` n `27`; metal avg `-0.0856` n `20`; unknown avg `0.1147` n `1256`
- 1h: commodity avg `-0.1079` n `13`; crypto_alt avg `0.0749` n `238`; crypto_major avg `0.2724` n `8`; equity avg `0.085` n `156`; fx avg `0.051` n `6`; index avg `0.0025` n `27`; metal avg `-0.0253` n `20`; unknown avg `1.0855` n `1256`
- 4h: commodity avg `-0.1653` n `13`; crypto_alt avg `-0.8339` n `238`; crypto_major avg `-0.2835` n `8`; equity avg `-0.0711` n `156`; fx avg `0.0785` n `6`; index avg `-0.0117` n `27`; metal avg `0.0282` n `20`; unknown avg `1.7097` n `1151`
- 24h: commodity avg `-0.5967` n `13`; crypto_alt avg `-1.766` n `238`; crypto_major avg `-0.2959` n `8`; equity avg `0.9268` n `156`; fx avg `0.2862` n `6`; index avg `0.298` n `27`; metal avg `0.0915` n `20`; unknown avg `2.5666` n `1065`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1843`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1763`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1746`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1679`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1507`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.138`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1347`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1201`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1195`, n `668`, weak_sample_signal
