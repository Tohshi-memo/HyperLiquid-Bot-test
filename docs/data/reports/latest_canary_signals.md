# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T08:37:11.846765+00:00`
- Correlation status: `ready`
- Asset price records: `630`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.02` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.159` n `12`; crypto_alt avg `0.1038` n `228`; crypto_major avg `0.0857` n `8`; equity avg `0.0512` n `65`; fx avg `0.0024` n `5`; index avg `0.0209` n `23`; metal avg `-0.0009` n `18`; unknown avg `0.2351` n `375`
- 1h: commodity avg `-0.1105` n `12`; crypto_alt avg `0.3572` n `228`; crypto_major avg `0.3062` n `8`; equity avg `0.5082` n `65`; fx avg `0.0059` n `5`; index avg `0.1554` n `23`; metal avg `0.2912` n `18`; unknown avg `0.6589` n `375`
- 4h: commodity avg `-0.4653` n `12`; crypto_alt avg `0.1861` n `228`; crypto_major avg `0.3475` n `8`; equity avg `0.8997` n `65`; fx avg `0.0543` n `5`; index avg `0.2714` n `23`; metal avg `0.5726` n `18`; unknown avg `0.7577` n `355`
- 24h: commodity avg `0.9318` n `12`; crypto_alt avg `0.6695` n `228`; crypto_major avg `-1.8517` n `8`; equity avg `-0.4997` n `65`; fx avg `0.2756` n `5`; index avg `-0.5799` n `23`; metal avg `-0.3406` n `18`; unknown avg `0.0423` n `355`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1317`, n `622`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1315`, n `622`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1128`, n `626`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1073`, n `626`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.102`, n `626`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0961`, n `626`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0854`, n `622`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0835`, n `622`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0755`, n `622`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0714`, n `626`, weak_sample_signal
