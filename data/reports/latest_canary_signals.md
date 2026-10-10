# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T12:37:24.373594+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0463` n `13`; crypto_alt avg `-0.0279` n `235`; crypto_major avg `0.0008` n `8`; equity avg `-0.0028` n `150`; fx avg `0.0015` n `6`; index avg `-0.0011` n `26`; metal avg `-0.0068` n `20`; unknown avg `0.0047` n `1117`
- 1h: commodity avg `0.0443` n `13`; crypto_alt avg `0.0808` n `235`; crypto_major avg `-0.0082` n `8`; equity avg `0.0139` n `150`; fx avg `0.006` n `6`; index avg `-0.0036` n `26`; metal avg `-0.0009` n `20`; unknown avg `0.2794` n `1109`
- 4h: commodity avg `-0.1864` n `13`; crypto_alt avg `-0.0448` n `235`; crypto_major avg `-0.1746` n `8`; equity avg `0.0324` n `150`; fx avg `-0.0106` n `6`; index avg `0.0111` n `26`; metal avg `-0.0002` n `20`; unknown avg `0.3337` n `1109`
- 24h: commodity avg `-0.1678` n `13`; crypto_alt avg `1.6816` n `235`; crypto_major avg `-0.1372` n `8`; equity avg `-0.1654` n `150`; fx avg `0.0314` n `6`; index avg `-0.0032` n `26`; metal avg `0.0593` n `20`; unknown avg `632.2597` n `954`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1543`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1411`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.12`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1151`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1043`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1025`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
