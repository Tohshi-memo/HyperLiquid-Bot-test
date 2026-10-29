# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T19:52:31.697188+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0987` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.082` n `13`; crypto_alt avg `-0.0228` n `238`; crypto_major avg `0.0325` n `8`; equity avg `0.1736` n `156`; fx avg `-0.0157` n `6`; index avg `0.0247` n `27`; metal avg `0.0283` n `20`; unknown avg `266.4435` n `1238`
- 1h: commodity avg `0.1` n `13`; crypto_alt avg `-0.1395` n `238`; crypto_major avg `-0.2289` n `8`; equity avg `0.2856` n `156`; fx avg `-0.0011` n `6`; index avg `0.0567` n `27`; metal avg `0.074` n `20`; unknown avg `2.9224` n `1232`
- 4h: commodity avg `0.2655` n `13`; crypto_alt avg `-1.6981` n `238`; crypto_major avg `-1.1244` n `8`; equity avg `-0.7857` n `156`; fx avg `-0.0108` n `6`; index avg `-0.0257` n `27`; metal avg `-0.0001` n `20`; unknown avg `5.4495` n `1228`
- 24h: commodity avg `-0.3647` n `13`; crypto_alt avg `-1.5204` n `238`; crypto_major avg `0.698` n `8`; equity avg `-1.7489` n `155`; fx avg `0.0247` n `6`; index avg `-0.1979` n `27`; metal avg `-0.5935` n `20`; unknown avg `10.5265` n `946`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0787`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0658`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0657`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0536`, n `668`, weak_sample_signal
