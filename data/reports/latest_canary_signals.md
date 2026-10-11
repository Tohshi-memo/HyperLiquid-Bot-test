# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T18:37:25.257960+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0075` n `13`; crypto_alt avg `0.0047` n `235`; crypto_major avg `-0.0294` n `8`; equity avg `-0.0016` n `150`; fx avg `0.0049` n `6`; index avg `-0.0001` n `26`; metal avg `0.0012` n `20`; unknown avg `-0.1264` n `1126`
- 1h: commodity avg `0.0287` n `13`; crypto_alt avg `-0.4177` n `235`; crypto_major avg `-0.4521` n `8`; equity avg `-0.0467` n `150`; fx avg `0.0014` n `6`; index avg `-0.0006` n `26`; metal avg `-0.0226` n `20`; unknown avg `0.2586` n `1122`
- 4h: commodity avg `0.1637` n `13`; crypto_alt avg `1.1057` n `235`; crypto_major avg `1.0078` n `8`; equity avg `0.2272` n `150`; fx avg `0.012` n `6`; index avg `0.0373` n `26`; metal avg `0.0336` n `20`; unknown avg `1.8518` n `1094`
- 24h: commodity avg `0.2853` n `13`; crypto_alt avg `2.0094` n `235`; crypto_major avg `0.9504` n `8`; equity avg `0.3334` n `150`; fx avg `0.0218` n `6`; index avg `0.0488` n `26`; metal avg `0.0738` n `20`; unknown avg `0.6577` n `909`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.142`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1329`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1099`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
