# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-18T19:52:32.423499+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.23` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0084` n `13`; crypto_alt avg `-0.2348` n `239`; crypto_major avg `-0.1402` n `8`; equity avg `-0.0897` n `164`; fx avg `-0.0045` n `6`; index avg `0.0021` n `27`; metal avg `0.0085` n `20`; unknown avg `0.9254` n `1265`
- 1h: commodity avg `0.1892` n `13`; crypto_alt avg `-0.5753` n `239`; crypto_major avg `-0.6512` n `8`; equity avg `-0.6069` n `164`; fx avg `-0.0163` n `6`; index avg `-0.0572` n `27`; metal avg `-0.1415` n `20`; unknown avg `0.3736` n `1263`
- 4h: commodity avg `0.1936` n `13`; crypto_alt avg `-0.1472` n `239`; crypto_major avg `-0.1772` n `8`; equity avg `0.0014` n `164`; fx avg `-0.0025` n `6`; index avg `0.0386` n `27`; metal avg `-0.0806` n `20`; unknown avg `4.2839` n `1257`
- 24h: commodity avg `0.0636` n `13`; crypto_alt avg `-0.1635` n `239`; crypto_major avg `-0.7493` n `8`; equity avg `0.2215` n `164`; fx avg `-0.1926` n `6`; index avg `0.0766` n `27`; metal avg `-1.1495` n `20`; unknown avg `-0.365` n `1138`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0719`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0672`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0576`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0574`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0566`, n `668`, weak_sample_signal
