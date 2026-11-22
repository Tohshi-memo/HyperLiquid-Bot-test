# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T03:37:24.114122+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3279` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0144` n `13`; crypto_alt avg `-0.1172` n `239`; crypto_major avg `-0.2173` n `8`; equity avg `-0.0216` n `166`; fx avg `0.0059` n `6`; index avg `-0.0039` n `27`; metal avg `-0.0176` n `20`; unknown avg `158.2129` n `1263`
- 1h: commodity avg `-0.0701` n `13`; crypto_alt avg `-0.5148` n `239`; crypto_major avg `-0.6912` n `8`; equity avg `-0.1371` n `166`; fx avg `0.0` n `6`; index avg `-0.0414` n `27`; metal avg `-0.0808` n `20`; unknown avg `256.3768` n `1263`
- 4h: commodity avg `-0.0971` n `13`; crypto_alt avg `-1.1406` n `239`; crypto_major avg `-1.4259` n `8`; equity avg `-0.3358` n `166`; fx avg `-0.0091` n `6`; index avg `-0.098` n `27`; metal avg `-0.1215` n `20`; unknown avg `176.9008` n `1256`
- 24h: commodity avg `-0.0229` n `13`; crypto_alt avg `2.1091` n `239`; crypto_major avg `3.7137` n `8`; equity avg `1.4314` n `166`; fx avg `-0.0225` n `6`; index avg `0.2005` n `27`; metal avg `0.1757` n `20`; unknown avg `237.4342` n `1082`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1443`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1259`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1133`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
