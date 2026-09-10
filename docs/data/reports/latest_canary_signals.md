# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T09:37:25.170003+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0827` n `12`; crypto_alt avg `-0.2475` n `233`; crypto_major avg `-0.1698` n `8`; equity avg `-0.0976` n `134`; fx avg `0.0151` n `6`; index avg `-0.0179` n `26`; metal avg `-0.0261` n `20`; unknown avg `0.2195` n `797`
- 1h: commodity avg `0.1118` n `12`; crypto_alt avg `-0.218` n `233`; crypto_major avg `-0.1869` n `8`; equity avg `-0.1895` n `134`; fx avg `0.0067` n `6`; index avg `-0.051` n `26`; metal avg `-0.0893` n `20`; unknown avg `0.3489` n `795`
- 4h: commodity avg `0.3103` n `12`; crypto_alt avg `-0.967` n `233`; crypto_major avg `-0.7225` n `8`; equity avg `-0.5773` n `134`; fx avg `0.0727` n `6`; index avg `-0.1073` n `26`; metal avg `-0.3267` n `20`; unknown avg `-0.3179` n `765`
- 24h: commodity avg `0.0623` n `12`; crypto_alt avg `-4.5167` n `233`; crypto_major avg `-3.0352` n `8`; equity avg `-1.2567` n `134`; fx avg `0.1154` n `6`; index avg `-0.1348` n `26`; metal avg `0.0338` n `20`; unknown avg `-0.5789` n `668`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1292`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1161`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
