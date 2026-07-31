# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T15:37:37.169285+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `1.7477` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0871` n `12`; crypto_alt avg `0.2232` n `230`; crypto_major avg `0.2005` n `8`; equity avg `0.0007` n `102`; fx avg `0.0287` n `6`; index avg `0.0047` n `25`; metal avg `-0.0115` n `20`; unknown avg `0.5078` n `780`
- 1h: commodity avg `-0.0999` n `12`; crypto_alt avg `0.0098` n `230`; crypto_major avg `-0.2204` n `8`; equity avg `-0.3541` n `102`; fx avg `0.0393` n `6`; index avg `0.0032` n `25`; metal avg `0.1017` n `20`; unknown avg `0.161` n `780`
- 4h: commodity avg `-0.1458` n `12`; crypto_alt avg `0.0725` n `230`; crypto_major avg `-0.7526` n `8`; equity avg `-2.5003` n `102`; fx avg `-0.0892` n `6`; index avg `-0.3141` n `25`; metal avg `-0.0199` n `20`; unknown avg `0.9546` n `780`
- 24h: commodity avg `0.0408` n `12`; crypto_alt avg `-0.5096` n `230`; crypto_major avg `-1.512` n `8`; equity avg `0.5608` n `102`; fx avg `0.1051` n `6`; index avg `0.2719` n `25`; metal avg `-0.1895` n `20`; unknown avg `1.3008` n `747`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1412`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1329`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0744`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0729`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0703`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0698`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0672`, n `668`, weak_sample_signal
