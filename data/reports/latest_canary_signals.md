# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T20:52:27.881591+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.92` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0205` n `12`; crypto_alt avg `-0.015` n `230`; crypto_major avg `-0.0392` n `8`; equity avg `0.0315` n `94`; fx avg `-0.002` n `6`; index avg `-0.0007` n `25`; metal avg `0.008` n `20`; unknown avg `0.1423` n `768`
- 1h: commodity avg `-0.0229` n `12`; crypto_alt avg `0.3436` n `230`; crypto_major avg `0.2296` n `8`; equity avg `0.0214` n `94`; fx avg `-0.0089` n `6`; index avg `0.0063` n `25`; metal avg `0.0202` n `20`; unknown avg `-0.0799` n `768`
- 4h: commodity avg `0.1751` n `12`; crypto_alt avg `0.2798` n `230`; crypto_major avg `0.0255` n `8`; equity avg `0.8777` n `94`; fx avg `0.0315` n `6`; index avg `0.2042` n `25`; metal avg `0.4293` n `20`; unknown avg `-0.3172` n `768`
- 24h: commodity avg `0.1207` n `12`; crypto_alt avg `0.6434` n `230`; crypto_major avg `0.8371` n `8`; equity avg `-0.4792` n `93`; fx avg `0.1981` n `6`; index avg `-0.1385` n `25`; metal avg `0.1787` n `20`; unknown avg `0.119` n `747`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1618`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1281`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1178`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1141`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0796`, n `668`, weak_sample_signal
