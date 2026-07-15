# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T21:37:34.122804+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0231` n `12`; crypto_alt avg `-0.072` n `230`; crypto_major avg `-0.1291` n `8`; equity avg `0.0043` n `94`; fx avg `0.0004` n `6`; index avg `-0.0036` n `25`; metal avg `0.0026` n `20`; unknown avg `-0.0299` n `768`
- 1h: commodity avg `-0.0418` n `12`; crypto_alt avg `-0.1026` n `230`; crypto_major avg `-0.109` n `8`; equity avg `-0.0783` n `94`; fx avg `0.0123` n `6`; index avg `-0.0174` n `25`; metal avg `-0.0054` n `20`; unknown avg `0.1839` n `768`
- 4h: commodity avg `0.2199` n `12`; crypto_alt avg `0.0049` n `230`; crypto_major avg `-0.2082` n `8`; equity avg `0.1639` n `94`; fx avg `0.0044` n `6`; index avg `0.0693` n `25`; metal avg `0.1805` n `20`; unknown avg `-0.2847` n `768`
- 24h: commodity avg `0.1372` n `12`; crypto_alt avg `0.4013` n `230`; crypto_major avg `0.5624` n `8`; equity avg `-0.6374` n `93`; fx avg `0.22` n `6`; index avg `-0.1657` n `25`; metal avg `0.1214` n `20`; unknown avg `0.0272` n `747`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1524`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1257`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.118`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1151`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1141`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
