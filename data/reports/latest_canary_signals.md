# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-18T10:41:07.443035+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0733` n `13`; crypto_alt avg `0.0297` n `239`; crypto_major avg `-0.2143` n `8`; equity avg `0.0531` n `163`; fx avg `0.0071` n `6`; index avg `0.011` n `27`; metal avg `0.0209` n `20`; unknown avg `0.4079` n `1266`
- 1h: commodity avg `0.0328` n `13`; crypto_alt avg `-0.0886` n `239`; crypto_major avg `-0.3856` n `8`; equity avg `-0.1873` n `163`; fx avg `0.0135` n `6`; index avg `-0.016` n `27`; metal avg `-0.0407` n `20`; unknown avg `4.6076` n `1260`
- 4h: commodity avg `0.0924` n `13`; crypto_alt avg `0.2311` n `239`; crypto_major avg `-0.1279` n `8`; equity avg `0.4792` n `163`; fx avg `-0.0551` n `6`; index avg `0.086` n `27`; metal avg `-0.2228` n `20`; unknown avg `117.1318` n `1186`
- 24h: commodity avg `-0.1091` n `13`; crypto_alt avg `1.1917` n `239`; crypto_major avg `1.2163` n `8`; equity avg `1.8841` n `163`; fx avg `-0.0885` n `6`; index avg `0.158` n `27`; metal avg `-0.9703` n `20`; unknown avg `5.7522` n `1099`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.075`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0705`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0686`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
