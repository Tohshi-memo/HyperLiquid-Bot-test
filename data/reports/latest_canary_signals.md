# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-18T06:52:34.362086+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0313` n `13`; crypto_alt avg `-0.0382` n `239`; crypto_major avg `-0.1722` n `8`; equity avg `-0.0127` n `163`; fx avg `0.004` n `6`; index avg `-0.0054` n `27`; metal avg `0.0124` n `20`; unknown avg `190.051` n `1264`
- 1h: commodity avg `-0.1696` n `13`; crypto_alt avg `0.0132` n `239`; crypto_major avg `-0.2933` n `8`; equity avg `-0.07` n `163`; fx avg `-0.0067` n `6`; index avg `-0.0061` n `27`; metal avg `-0.1057` n `20`; unknown avg `0.4726` n `1244`
- 4h: commodity avg `-0.2679` n `13`; crypto_alt avg `0.5795` n `239`; crypto_major avg `0.406` n `8`; equity avg `0.8959` n `163`; fx avg `0.0165` n `6`; index avg `0.14` n `27`; metal avg `-0.1456` n `20`; unknown avg `3.318` n `1224`
- 24h: commodity avg `-0.0427` n `13`; crypto_alt avg `0.395` n `239`; crypto_major avg `0.4678` n `8`; equity avg `0.6959` n `163`; fx avg `-0.0906` n `6`; index avg `0.0254` n `27`; metal avg `-0.8571` n `20`; unknown avg `492.2254` n `1071`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1067`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.064`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0572`, n `668`, weak_sample_signal
